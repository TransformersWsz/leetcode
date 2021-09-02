#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 12:48 AM
# @Author  : Swift
# @File    : course-schedule.py
# @Link    : https://leetcode-cn.com/problems/course-schedule/
# @Desc    : 207. 课程表
# @Method  : https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/

class Solution:
    def __init__(self):
        self.can_finish_courses = True

    def dfs(self, cource_id, visited, edges):
        visited[cource_id] = 1
        for v in edges[cource_id]:
            if not visited[v]:
                self.dfs(v, visited, edges)
                if not self.can_finish_courses:
                    return
            elif visited[v] == 1:
                self.can_finish_courses = False
                return
        visited[cource_id] = 2

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses

        for a, b in prerequisites:
            edges[b].append(a)

        for i in range(numCourses):
            if self.can_finish_courses and not visited[i]:
                self.dfs(i, visited, edges)
        return self.can_finish_courses