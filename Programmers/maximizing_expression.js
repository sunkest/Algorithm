function solution(expression) {
  const numbers = [];
  const operands = ['/']; // 편의를 위해 index 1부터 시작
  let currentNum = '';
  for (const ch of expression) {
    if (ch === '+' || ch === '-' || ch === '*') {
      numbers.push(Number(currentNum));
      currentNum = '';
      operands.push(ch);
    } else {
      currentNum += ch;
    }
  }
  numbers.push(Number(currentNum));
  const permutations = ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*'];
  const results = [];
  for (const priority of permutations) {
    const tempNums = numbers.slice();
    const tempOperands = operands.slice();
    for (const targetOp of priority) {
      for (let i=1; i<operands.length; i++) {
        const op = tempOperands[i];
        if (op === targetOp) {
          let result = 0;
          if (op === '+') {
            result = tempNums[i-1] + tempNums[i];
          } else if (op === '-') {
            result = tempNums[i-1] - tempNums[i];
          } else if (op === '*') {
            result = tempNums[i-1] * tempNums[i];
          }
          tempNums.splice(i-1, 2, result);
          tempOperands.splice(i, 1);
          i--;
        }
      }
    }
    results.push(Math.abs(tempNums[0]));
  }
  const answer = Math.max(...results);

  return answer;
}

const expression = '50*6-3*2';
console.log(solution(expression));
