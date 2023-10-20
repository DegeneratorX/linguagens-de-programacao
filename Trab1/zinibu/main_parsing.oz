functor
import
	Browser
	parsing at 'parsing.ozf'

	define
		A Sn
		A={parsing.prog
		   [program foo ';' while a '+' 3 '<' b 'do' b ':=' b '+' 1 'end']
		   Sn}
		{Browser.browse A}
	
end
