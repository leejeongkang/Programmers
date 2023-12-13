function solution(skill, skill_trees) {
    let answer = 0;
    for(let skillTree of skill_trees) {
        let split = skill.split('');
        let cnt = 0;
        
        for(let i in skillTree) {
           if(split.includes(skillTree[i])) {
                if(skillTree[i] !== split.shift()) {
                    break;
                }
                else cnt++;
            }
            else cnt++;
        }

        if(cnt === skillTree.length) {
            answer++;
        }
    }
    return answer;
}