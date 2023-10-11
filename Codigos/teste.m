%
%
% Trabalho de transmissao digital - Prof. Diniz
% Aluno: Fernando Dias
%
% 


%% Definiçao de parametros (M >> K >> 1)
K = 20;   % Numero de clientes (transmissores)
M = 100;  % Numero de antenas (receptores na BS)


%% Definiçao do canal
H_real = random('normal',zeros([M,K]),ones([M,K]))+1i*random('normal',zeros([M,K]),ones([M,K]));

 

%% 
%
% 
%
function [R] = Quantizador(Y)
    R = qammod(Y,4);
end

function [Y] = CanalMimo(H,s,phi_d)
    
    n = random('normal',zeros(M),ones(M));
    n = n/norm(n);

    Y = sqrt(phi_d)*H*s+n;
end
