class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        if (n === 1){
            return 1;
        } else if (n === 2){
            return 2;
        }
        return this.climbStairs(n-1) + this.climbStairs(n-2);
    }
}
