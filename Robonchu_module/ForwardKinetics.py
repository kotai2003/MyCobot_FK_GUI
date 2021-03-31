import numpy as np

#https://github.com/Robonchu/PythonSimpleManipulation

def skew_mat(vector):
    mat = np.zeros((3, 3))
    mat[0, 1] = -vector[2]
    mat[0, 2] = vector[1]
    mat[1, 0] = vector[2]
    mat[1, 2] = -vector[0]
    mat[2, 0] = -vector[1]
    mat[2, 1] = vector[0]
    return mat

def rodrigues_mat(vector, angle):
    mat = np.eye(3) + skew_mat(vector) * np.sin(angle) + skew_mat(
        vector) @ skew_mat(vector) * (1.0 - np.cos(angle))
    return mat

def calc_fk(angles, vectors, lengths, dof=6):
    iter_num = dof + 1
    pos = [0, 0, 0]
    R = np.eye(3)
    pos_list = np.zeros((dof + 2, 3))
    R_list = np.zeros((dof + 2, 3, 3))
    pos_list[0] = pos
    R_list[0] = R
    # Calculate Forward Kinematics
    for i in range(iter_num):
        pos = pos + R @ lengths[i].T
        R = R @ rodrigues_mat(vectors[i], angles[i])
        pos_list[i + 1] = pos
        R_list[i + 1] = R
    return pos, R, pos_list, R_list
