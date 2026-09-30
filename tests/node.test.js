import test from 'node:test';
import assert from 'node:assert/strict';
import {sum} from '../src/math.js';
for(const [a,b,result] of [[1,2,3],[0,0,0],[-1,1,0],[3,4,7]])test(`sum ${a} ${b}`,()=>assert.equal(sum(a,b),result));
