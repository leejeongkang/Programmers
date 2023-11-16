function solution(priorities, location) {
    let answer = 0;
    const queue = priorities.map((val, index) => ({ val, index }));

    while (1) {
        const current = queue.shift();
        if (queue.some(item => item.val > current.val)) {
            queue.push(current);
            console.log(current)
             console.log(queue)
        } else {
            answer++;
            console.log(answer)
            if (current.index === location) {
                break;
            }
        }
    }

    return answer;
}