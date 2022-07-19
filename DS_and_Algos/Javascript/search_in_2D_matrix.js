var searchMatrix = function (matrix, target) {
  if (matrix[0] === undefined) {
    return false;
  }

  let min = 0;
  let max = matrix[0].length - 1;

  while (min <= max) {
    let mid = Math.floor((min + max) / 2);

    if (matrix[0][mid] === target) {
      return true;
    } else if (matrix[0][mid] > target) {
      max = mid - 1;
    } else min = mid + 1;
  }

  matrix.splice(0, 1);
  return searchMatrix(matrix, target);
};

console.log(
  "searchMatrix",
  searchMatrix(
    [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 50],
    ],
    33
  )
);
