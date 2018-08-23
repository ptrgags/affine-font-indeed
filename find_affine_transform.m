% Find the coefficients of A and b in the equation
% Ax + b
% before and after are two matrices of points.
% before is 2 x N, after is 2 x N
% the points are column vectors.
function [A, b] = find_affine_transform(before, after)
    % Bias the before matrix to allow for translations
    lhs = before';
    lhs(:, end + 1) = 1;
    
    % calculate all 6 coefficients at once:
    rhs = after';
    coefficients = lhs \ rhs;
    
    % Split into A and b
    A = coefficients(1:end - 1, :)';
    b = coefficients(end, :)';
end