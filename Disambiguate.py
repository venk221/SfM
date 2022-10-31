import numpy as np

def DisambiguateCameraPose(C_all, R_all, X_all):

    max_points=0
    best_index=0

    for i in range(4):

        num_world_points=X_all[i].shape[0]

        num_points_satisfying_condtion=0

        for j in range(num_world_points):

            r3=R_all[i][2,:]
            this_image_world_points=X_all[i]

            

            if (np.dot(r3,this_image_world_points[j,:]-C_all[i])):

                num_points_satisfying_condtion+=1

        if num_points_satisfying_condtion>max_points:
            max_points=num_points_satisfying_condtion
            best_index=i



    return C_all[best_index],R_all[best_index],X_all[best_index]
