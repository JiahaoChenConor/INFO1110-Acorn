## About the hardest part

1. For the first semester of freshman, it is not very difficult to implement this game, except for finding a feasible path with DFS and finding the shortest path with BFS.

   ## DFS

   For dfs, there is list stores the grids the player has walked and the player can no longer walk into

   these grids.

   When water is obtained, clear the list which stores the grids has went so that the player can go back to prevent being trapped in the dead end.

   ![image-20201119223204840](/Users/mac/Library/Application Support/typora-user-images/image-20201119223204840.png)		 						 		

   ## BFS

   There are two many conditions for finding the shortest way for this game. When I came up with a "perfect idea", I always thought of damn counterexamples at some moment. I still have no idea how to finish it by a perfect way. But luckily my stupid method has passed all the test cases. 

   ```
       #  First use bfs to find how much fire is needed
       #  Find all water objects and store them in the list []
       #  for example, there is three fire on the shortest way to End, and there are five waters on the map
       #  Pick five out of three for full arrangement
       #  Then pick up the "shortest" way
   ```

   If you have any idea, welcome to discuss.  👏