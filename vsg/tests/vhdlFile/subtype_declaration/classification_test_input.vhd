
architecture RTL of FIFO is


  subtype DIGITS is INTEGER range 0 to 9;

  subtype BIT_NEW is RESOLVE_VALUE BIT;

  -- EXAMPLE 1 : a resolved subtype
  subtype MY_STD_LOGIC is Resolved Std_ulogic;

  -- EXAMPLE 2: an integer subtype
  subtype MyBit is STD_LOGIC range '0' to '1';

  -- EXAMPLE 3 : an array subtype
  subtype ShortVector is STD_LOGIC_VECTOR(1 downto 0);

  subtype new_std_logic is (resolved) std_ulogic;

begin

end architecture RTL;
