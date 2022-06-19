/**
 * Returns a random number between min (inclusive) and max (exclusive)
 */
export const getRandomArbitrary = function (min, max) {
  return Math.floor(Math.random() * (max - min) + min);
};
