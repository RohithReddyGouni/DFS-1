class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Que=deque()
        m=len(image)
        n=len(image[0])
        color_tbc=image[sr][sc]
        
        if color_tbc !=color:
            Que.append((sr,sc))
        image[sr][sc]=color
        visited=set((sr,sc))
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        while Que:
            row,col=Que.popleft()
            for nr,nc in directions:
                nr=row+nr
                nc=col+nc
                if nr>=0 and nr < m and nc>=0 and nc<n and (nr,nc) not in visited and image[nr][nc]==color_tbc:
                    image[nr][nc]=color
                    Que.append((nr,nc))
                    visited.add((nr,nc))
        return image
                    
    