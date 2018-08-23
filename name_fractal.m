% Big rectangle
BIG_RECT = [
    0 0 34;
    0 10 0;
];

% Letter P: 3 transforms
P1 = [
    0 2 0;
    10 10 0;
];
P2 = [
    2 2 6;
    8 10 7;
];
P3 = [
    2 2 6;
    4 6 5;
];

[A_P1, b_P1] = find_affine_transform(BIG_RECT, P1);
[A_P2, b_P2] = find_affine_transform(BIG_RECT, P2);
[A_P3, b_P3] = find_affine_transform(BIG_RECT, P3);

% E Shape
E1 = [
    0 0 6;
    8 10 8
];
E2 = [
    0 2 0;
    8 8 2
];
E3 = [
    2 2 6;
    4 6 4
];
E4 = [
    0 0 6;
    0 2 0
];

[A_E1, b_E1] = find_affine_transform(BIG_RECT, E1);
[A_E2, b_E2] = find_affine_transform(BIG_RECT, E2);
[A_E3, b_E3] = find_affine_transform(BIG_RECT, E3);
[A_E4, b_E4] = find_affine_transform(BIG_RECT, E4);

ET1 = [7; 0];
ET2 = [21; 0];

% T shape
T1 = [
    0 0 6;
    8 10 8;
];
T2 = [
    2 4 2;
    8 8 0;
];

[A_T1, b_T1] = find_affine_transform(BIG_RECT, T1);
[A_T2, b_T2] = find_affine_transform(BIG_RECT, T2);

TT = [14; 0];

% R shape
R1 = [
    0 2 0;
    10 10 0;
];
R2 = [
    2 2 6;
    8 10 7;
];
R3 = [
    2 2 6;
    4 6 5
];
R4 = [
    3 5 4;
    4 5 0;
];

[A_R1, b_R1] = find_affine_transform(BIG_RECT, R1)
[A_R2, b_R2] = find_affine_transform(BIG_RECT, R2)
[A_R3, b_R3] = find_affine_transform(BIG_RECT, R3)
[A_R4, b_R4] = find_affine_transform(BIG_RECT, R4)