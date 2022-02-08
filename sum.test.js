const sum = require('./sum');

test('adds 1 plus 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(4);
});