const test = require('tape');
const from = require('./index').from;
const to = require('./index').to;
const add = require('./index').add;
const subtract = require('./index').subtract;


test('converts letters to numbers', (t) => {
  t.plan(11);

  t.equals(from('a'), 1);
  t.equals(from('j'), 10);
  t.equals(from('z'), 26);
  t.equals(from('aa'), 27);
  t.equals(from('aj'), 36);
  t.equals(from('az'), 52);
  t.equals(from('ba'), 53);
  t.equals(from('zz'), 702);
  t.equals(from('aaa'), 703);
  t.throws(() => from('A'), 703, 'Should not handle any characters besides a-z');
  t.throws(() => from(''), 703, 'Should not handle empty string');
});


test('converts numbers to letters', (t) => {
  t.plan(9);

  t.equals(to(1), 'a');
  t.equals(to(10), 'j');
  t.equals(to(26), 'z');
  t.equals(to(27), 'aa');
  t.equals(to(36), 'aj');
  t.equals(to(52), 'az');
  t.equals(to(53), 'ba');
  t.equals(to(702), 'zz');
  t.equals(to(703), 'aaa');
});

test('performs math', (t) => {
  t.plan(8);

  t.equals(add('b', 10), 'l', 'Should add with single digit');
  t.equals(add('aab', 10), 'aal', 'Should add with multiple digits');
  t.equals(add('x', 5), 'ac', 'Should add with carry');
  t.equals(add('zc', 27), 'aad', 'Should add with multiple digits and carry');
  t.equals(subtract('g', 5), 'b', 'Should subtract');
  t.equals(subtract('aag', 5), 'aab', 'Should subtract with multiple digits');
  t.equals(subtract('aag', 29), 'zd', 'Should subtract with multiple digits and carry');
  t.throws(() => subtract('aa', 27), 'Should not handle negative results');
});
