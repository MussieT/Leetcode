var merge = function (intervals) {
  if (intervals.length === 0) {
    return [];
  }

  intervals.sort((a, b) => a[0] - b[0]);

  let merged = [];
  let exists = false;
  for (let i = 0; i < intervals.length; i++) {
    if (intervals[i + 1] && intervals[i][1] >= intervals[i + 1][0]) {
      exists = true;
      merged.push([
        intervals[i][0],
        Math.max(intervals[i + 1][1], intervals[i][1]),
      ]);
      i += 1;
      continue;
    }
    merged.push(intervals[i]);
  }

  if (exists) return merge(merged);

  return merged;
};
