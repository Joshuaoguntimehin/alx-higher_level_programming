#!/usr/bin/node
const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else if (args[1] === undefined) {
  console.log(args[0]);
} else {
  args.forEach((arg, index) => {
    console.log(`${index + 1}: ${arg}`);
  });
}
