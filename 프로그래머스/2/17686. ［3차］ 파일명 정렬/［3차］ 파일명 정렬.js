function solution(files) {
 const pattern = /(\D+)(\d{1,5})/;   
    
 const file = "abc123.txt"
 let matchFile = file.match(pattern);
 //console.log(matchFile)
    /*
   [
       'abc123',
       'abc',
       '123',
       index: 0,
       input: 'abc123.txt',
       groups: undefined
   ]
   */
    //'\D+' : 숫자가 아닌 문자열
    //'\d{1,5}' : 1에서 5자리의 숫자
    // 0 ~ 99999
   
  return files.sort((a, b) => {
    let [aHead, aNumber] = a.match(pattern).slice(1, 3);
    let [bHead, bNumber] = b.match(pattern).slice(1, 3);
    aHead = aHead.toLowerCase();
    bHead = bHead.toLowerCase();
      // 대문자 -> 소문자
    if (aHead === bHead && aNumber === bNumber) return 0;
    if (aHead === bHead) return aNumber - bNumber;
      // 문자열 같으면 숫자 부분 기준으로 오름차순 정렬
    if (aHead > bHead) return 1;
    else return -1;
  });
 
}