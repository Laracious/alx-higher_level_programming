#!/usr/bin/node

// script that prints the first argument passed to it


const args = process.argv;
if (args[3]) {
	console.log(args[3]);
} else {
	console.log('No argument');
}
