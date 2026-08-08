#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const nums = args.map(x => Number.parseInt(x, 10));
  const sortedUnique = Array.from(new Set(nums)).sort((a, b) => b - a);
  console.log(sortedUnique[1] !== undefined ? sortedUnique[1] : 0);
}
