Considere o programa abaixo, escrito na linguagem núcleo do modelo declarativo, o qual descreve a computação de um MDC (máximo divisor comum) entre dois números inteiros. Responda:

- Escreva uma versão mais abreviada e natural possível desse programa usando açúcares sintáticos e abstrações linguísticas da linguagem estendida. Descreva como fez o mapeamento, mesmo que informalmente, listando os açúcares sintáticos e abstrações linguísticas empregados.

- Qual o efeito da execução desse programa? Mostre argumentando formalmente sobre a execução na máquina abstrata (mostre os passos relevantes, de forma simplificada, explicando a transição de um passo para o outro).

```
local MDC in 
    MDC = proc {$ A B ?R}
        local T1 in 
            {'==' A B T1}
            if T1 then R=A
                else local T2 in 
                    {'>' A B T2}
                    if T2 then local C in {'-' A B C} {MDC C B R} end
                        else {MDC B A R}
                    end
                end
            end
        end
    end
    local X in local Y in local Z in X=6 Y=4 {MDC X Y Z} {Browse Z} end end end
end


```