function solution(new_id) {
  const str1 = new_id.toLowerCase();

  const str2 = str1.split(/[^a-z0-9-_.]/).join("");

  const str3 = str2.split(/[.]{2,}/).join(".");

  let str4 = str3;
  if (str3[0] === ".") {
    str4 = str3.slice(1);
  }
  if (str3.slice(-1) === ".") {
    str4 = str4.slice(0, -1);
  }

  let str5 = str4;
  if (str4.length === 0) {
    str5 = "a";
  }

  let str6 = str5;
  if (str5.length >= 16) {
    str6 = str5.slice(0, 15);
    if (str6.slice(-1) === ".") {
      str6 = str6.slice(0, -1);
    }
  }

  let str7 = str6;
  const end = str7.slice(-1);
  while (str7.length <= 2) {
    str7 += end;
  }

  return str7;
}

console.log(solution("...!@BaT#*..y.abcdefghijklm.."));
