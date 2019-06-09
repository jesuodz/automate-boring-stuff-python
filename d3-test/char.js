const margin = {top:10, bottom: 30, right: 40, left: 30},
      width = 450 - margin.left - margin.right,
      height = 400 - margin.bottom - margin.top;

let svg = d3.select("#vis_area")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.bottom + margin.top)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

// Crea la escala: transforma valor a pixel
let x = d3.scaleLinear()
  .domain([-7, 7])
  .range([0, width]);
svg
  .append('g')
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x));

let y = d3.scaleLinear()
  .domain([-7, 7])
  .range([height, 0]);
svg
  .append('g')
  .call(d3.axisRight(y))

svg
  .selectAll("whatever")
  .data(data)
  .enter()
  .append("circle")
    .attr("cx", function(d){ return x(d.x) })
    .attr("cy", function(d){ return y(d.y) })
    .attr("r", 1)