const from = exports.from = (alpha) => {
  if (!/^[a-z]+$/.test(alpha)) {
    throw new Error('Input must be a non-empty string comprised of only characters a-z')
  }

  const letters = alpha.split('');
  let out = 0;

  for (let i = 0; i < letters.length; i++) {
    out += (letters[letters.length - 1 - i].charCodeAt() - 96) * Math.pow(26, i);
  }

  return out;
};


const to = exports.to = (decimal) => {
  if (decimal <= 0) {
    throw new Error('Number must be > 0');
  }

  let out = '';

  while (true) {
    out = String.fromCharCode(((decimal - 1) % 26) + 97) + out;
    decimal = Math.floor((decimal - 1) / 26);

    if (decimal === 0) {
      break;
    }
  }

  return out;
};


exports.add = (alpha, num) => to(from(alpha) + num);

exports.subtract = (alpha, num) => to(from(alpha) - num);
