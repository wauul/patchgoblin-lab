import test from 'node:test';
import assert from 'node:assert/strict';
import {multiply} from '../src/math.ts';
test('widget multiplication',()=>assert.equal(multiply(6,7),42));
