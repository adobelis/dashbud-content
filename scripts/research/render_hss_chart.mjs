#!/usr/bin/env node
/**
 * Render an ECharts chart from a Dashbud conversation's content_struct.
 * Outputs SVG to the HSS assets directory.
 *
 * Usage:
 *   node render_hss_chart.mjs <conversation_id> [--message <index>] [--output <filename>]
 *   node render_hss_chart.mjs 102 --message 1 --output forge-frame-revenue-by-channel.svg
 *   node render_hss_chart.mjs 102 --list   # list messages with charts
 *
 * Requires: pg, echarts
 *   npm install pg echarts
 */

import pg from 'pg';
import * as echarts from 'echarts';
import { writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';

const ASSETS_DIR = '/Users/arthur/www/dashbud/website/dashbud-home-astro-01/public/assets/hss';

const pool = new pg.Pool({
  host: 'localhost',
  port: 5432,
  database: 'dashbud_local',
  user: 'postgres',
  password: 'postgres',
});

// ── Dashbud color palette (matches MODERN_COLORS from app theme) ──
const COLORS = [
  '#5470c6', '#91cc75', '#fac858', '#ee6666',
  '#73c0de', '#3ba272', '#fc8452', '#9a60b4',
  '#ea7ccc', '#4dc9f6',
];

// ── Color utils ──
function hexToRgb(hex) {
  const h = hex.replace('#', '');
  const n = parseInt(h, 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}

function lighten(hex, amount = 0.15) {
  const [r, g, b] = hexToRgb(hex);
  const lr = Math.min(255, Math.round(r + (255 - r) * amount));
  const lg = Math.min(255, Math.round(g + (255 - g) * amount));
  const lb = Math.min(255, Math.round(b + (255 - b) * amount));
  return `rgb(${lr},${lg},${lb})`;
}

function makeBarGradient(color) {
  return new echarts.graphic.LinearGradient(0, 0, 0, 1, [
    { offset: 0, color: lighten(color, 0.30) },
    { offset: 1, color: color },
  ]);
}

// ── Build ECharts option from content_struct ──
// opts.seriesOrder: array of series names in desired order, e.g. ['Northeast','Southeast','Midwest','West','Pacific NW']
function buildOption(struct, opts = {}) {
  const { data, chartSuggestion, column_metadata } = struct;
  if (!data || !chartSuggestion) return null;

  const { xField, yField, seriesField, suggestedChartType } = chartSuggestion;
  const yFields = Array.isArray(yField) ? yField : [yField];
  const chartType = opts.chartType || suggestedChartType || 'bar';

  // Get column metadata for formatting
  const colMeta = {};
  if (column_metadata) {
    for (const cm of column_metadata) {
      colMeta[cm.name] = cm;
    }
  }

  // Build x-axis categories
  const xData = data[xField] || [];
  const rowCount = xData.length;

  // If there's a secondary grouping field (like quarter within year), combine them
  let xLabels = xData;
  const hasQuarter = data['quarter'] && xField === 'year';
  if (hasQuarter) {
    xLabels = xData.map((v, i) => `${v} Q${data['quarter'][i]}`);
  }

  // Determine unique x values, sorted chronologically
  const uniqueX = [...new Set(xLabels)].sort((a, b) => {
    // Try date parsing first
    const da = new Date(a), db = new Date(b);
    if (!isNaN(da.getTime()) && !isNaN(db.getTime())) return da - db;
    // Fall back to string sort (handles "2024 Q1" etc.)
    return String(a).localeCompare(String(b));
  });
  // Formatted labels for display
  const displayX = uniqueX.map(formatDateLabel);

  let series = [];
  let legend = undefined;

  if (seriesField && data[seriesField]) {
    // Grouped/series chart
    let seriesValues = [...new Set(data[seriesField])];
    if (opts.seriesOrder) {
      seriesValues = opts.seriesOrder.filter(s => seriesValues.includes(s));
      // Append any values not in the custom order
      for (const sv of [...new Set(data[seriesField])]) {
        if (!seriesValues.includes(sv)) seriesValues.push(sv);
      }
    }
    legend = {
      top: 0,
      left: 'center',
      type: 'scroll',
      pageIconSize: 10,
      pageTextStyle: { fontSize: 10 },
      icon: 'rect',
      itemWidth: 14,
      itemHeight: 14,
      textStyle: { fontSize: 11, color: '#555' },
      itemGap: 16,
    };

    for (let si = 0; si < seriesValues.length; si++) {
      const sv = seriesValues[si];
      const seriesData = uniqueX.map(xVal => {
        // Find rows matching this x value and series value
        let total = 0;
        for (let i = 0; i < rowCount; i++) {
          if (xLabels[i] === xVal && data[seriesField][i] === sv) {
            for (const yf of yFields) {
              total += parseFloat(data[yf][i]) || 0;
            }
          }
        }
        return total;
      });

      const color = COLORS[si % COLORS.length];
      series.push({
        name: capitalize(sv),
        type: chartType === 'bar' ? 'bar' : 'line',
        data: seriesData,
        itemStyle: {
          color: chartType === 'bar' ? makeBarGradient(color) : color,
          borderRadius: chartType === 'bar' ? [3, 3, 0, 0] : undefined,
        },
        barMaxWidth: 36,
        barGap: '20%',
        emphasis: { itemStyle: { color: lighten(color, 0.25) } },
        ...(chartType === 'area' ? { areaStyle: { opacity: 0.3 } } : {}),
      });
    }
  } else {
    // Simple chart — one series per yField
    for (let yi = 0; yi < yFields.length; yi++) {
      const yf = yFields[yi];
      const seriesData = uniqueX.map(xVal => {
        let total = 0;
        for (let i = 0; i < rowCount; i++) {
          if (xLabels[i] === xVal) {
            total += parseFloat(data[yf][i]) || 0;
          }
        }
        return total;
      });

      const color = COLORS[yi % COLORS.length];
      series.push({
        name: capitalize(yf),
        type: chartType === 'bar' ? 'bar' : 'line',
        data: seriesData,
        itemStyle: {
          color: chartType === 'bar' ? makeBarGradient(color) : color,
          borderRadius: chartType === 'bar' ? [3, 3, 0, 0] : undefined,
        },
        barMaxWidth: 36,
        barGap: '20%',
        emphasis: { itemStyle: { color: lighten(color, 0.25) } },
        ...(chartType === 'area' ? { areaStyle: { opacity: 0.3 } } : {}),
      });
    }
  }

  // Format y-axis based on column metadata
  const yMeta = colMeta[yFields[0]];
  const isCurrency = yMeta?.units?.format?.includes('$');

  const showLegend = series.length > 1;
  const gridTop = showLegend ? 36 : 12;

  const option = {
    backgroundColor: '#ffffff',
    animation: false,
    grid: {
      left: 80,
      right: 24,
      top: gridTop,
      bottom: displayX.length > 12 ? 70 : displayX.length > 8 ? 60 : 32,
      containLabel: false,
    },
    xAxis: {
      type: 'category',
      data: displayX,
      axisLabel: {
        fontSize: 10,
        color: '#6b7280',
        rotate: displayX.length > 12 ? 45 : displayX.length > 8 ? 30 : 0,
        interval: displayX.length > 24 ? 2 : displayX.length > 12 ? 1 : 0,
      },
      axisLine: { lineStyle: { color: '#e5e7eb' } },
      axisTick: { show: false },
    },
    yAxis: {
      type: 'value',
      axisLabel: {
        fontSize: 11,
        color: '#6b7280',
        formatter: isCurrency
          ? (v) => v >= 1000000 ? `$${(v / 1000000).toFixed(1)}M` : v >= 1000 ? `$${(v / 1000).toFixed(0)}K` : `$${v}`
          : undefined,
      },
      axisLine: { show: false },
      axisTick: { show: false },
      splitLine: { lineStyle: { color: '#f3f4f6' } },
    },
    legend: showLegend ? legend : undefined,
    series,
    tooltip: { show: false },  // static image, no tooltip
  };

  return option;
}

function capitalize(s) {
  return s.charAt(0).toUpperCase() + s.slice(1);
}

const MONTH_ABBR = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

function formatDateLabel(val) {
  // Handle ISO dates like "2023-01-01T00:00:00"
  if (typeof val === 'string' && val.match(/^\d{4}-\d{2}/)) {
    const d = new Date(val);
    return `${MONTH_ABBR[d.getMonth()]} ${d.getFullYear()}`;
  }
  return String(val);
}

// ── Render to SVG ──
function renderSvg(option, width = 680, height = 320) {
  const chart = echarts.init(null, null, {
    renderer: 'svg',
    ssr: true,
    width,
    height,
  });
  chart.setOption(option);
  const svg = chart.renderToSVGString();
  chart.dispose();
  return svg;
}

// ── DB queries ──
async function listChartMessages(convId) {
  const res = await pool.query(`
    SELECT cm.id, cm.created_at::timestamp(0),
           substring(cm.content_text, 1, 80) as preview,
           cm.content_struct->'chartSuggestion'->'suggestedChartType' as chart_type
    FROM conversation_message cm
    WHERE cm.conversation_id = $1
      AND cm.role = 'assistant'
      AND cm.content_struct IS NOT NULL
      AND cm.content_struct::text LIKE '%chartSuggestion%'
    ORDER BY cm.created_at
  `, [convId]);

  console.log(`Messages with charts in conversation ${convId}:\n`);
  res.rows.forEach((r, i) => {
    console.log(`  [${i}] id=${r.id} | ${r.chart_type} | ${r.preview}...`);
  });
  return res.rows;
}

async function getChartMessage(convId, messageIndex) {
  const res = await pool.query(`
    SELECT cm.id, cm.content_text, cm.content_struct
    FROM conversation_message cm
    WHERE cm.conversation_id = $1
      AND cm.role = 'assistant'
      AND cm.content_struct IS NOT NULL
      AND cm.content_struct::text LIKE '%chartSuggestion%'
    ORDER BY cm.created_at
  `, [convId]);

  if (messageIndex >= res.rows.length) {
    console.error(`Only ${res.rows.length} chart messages found, index ${messageIndex} out of range`);
    process.exit(1);
  }

  return res.rows[messageIndex];
}

// ── Main ──
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Usage: node render_hss_chart.mjs <conv_id> [--list] [--message <idx>] [--output <name.svg>] [--width <px>] [--height <px>] [--series-order "A,B,C"]');
    process.exit(0);
  }

  const convId = parseInt(args[0]);
  const doList = args.includes('--list');
  const msgIdx = args.includes('--message') ? parseInt(args[args.indexOf('--message') + 1]) : 0;
  const outputName = args.includes('--output') ? args[args.indexOf('--output') + 1] : null;
  const width = args.includes('--width') ? parseInt(args[args.indexOf('--width') + 1]) : 680;
  const height = args.includes('--height') ? parseInt(args[args.indexOf('--height') + 1]) : 320;

  if (doList) {
    await listChartMessages(convId);
    await pool.end();
    return;
  }

  const msg = await getChartMessage(convId, msgIdx);
  const struct = msg.content_struct;

  console.log(`Building chart from message ${msg.id}...`);
  console.log(`  Chart type: ${struct.chartSuggestion?.suggestedChartType}`);
  console.log(`  X: ${struct.chartSuggestion?.xField}, Y: ${struct.chartSuggestion?.yField}, Series: ${struct.chartSuggestion?.seriesField}`);
  console.log(`  Rows: ${struct.data?.[struct.columns?.[0]]?.length || '?'}`);

  const seriesOrder = args.includes('--series-order') ? args[args.indexOf('--series-order') + 1].split(',') : null;
  const option = buildOption(struct, { seriesOrder });
  if (!option) {
    console.error('Could not build chart option');
    process.exit(1);
  }

  const svg = renderSvg(option, width, height);

  mkdirSync(ASSETS_DIR, { recursive: true });
  const filename = outputName || `chart-${convId}-${msgIdx}.svg`;
  const outPath = join(ASSETS_DIR, filename);
  writeFileSync(outPath, svg);
  console.log(`Wrote ${outPath} (${svg.length} chars)`);

  await pool.end();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
