export const genUniqKey = () => {
  return (
    Math.random().toString(16).substr(2, 4) +
    Math.random().toString(16).substr(2, 5)
  );
};
