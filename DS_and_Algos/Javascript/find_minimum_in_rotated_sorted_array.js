var findMin = function (nums) {
  let min = 0;
  let max = nums.length - 1;
  let mid;

  if (nums.length === 1 || nums[min] < nums[max]) {
    return nums[0];
  }

  while (min <= max) {
    let mid = Math.floor((min + max) / 2);

    if (nums[mid] < nums[mid - 1]) {
      return nums[mid];
    }

    if (nums[mid] > nums[max]) {
      min = mid + 1;
    } else {
      max = mid - 1;
    }
  }
  return mid;
};

console.log(findMin([1, 2]));
