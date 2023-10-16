function solution(numbers) {
    let list = numbers.sort((a,b)=> b - a )

    return list[0] * list [1]
}