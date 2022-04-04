names = [("com.supercell.scroll.rumblebundle0", "Kings Cup Package $0.99"), ("com.supercell.scroll.rumblebundle1", "Kings Cup Package $4.99"), ("com.supercell.scroll.rumblebundle2", "Kings Cup Package $9.99"),
         ('com.supercell.scroll.red', '(RED) pack $4.99'), ('com.supercell.scroll.consumableholidaypack0', 'Holiday pack $4.99'), ('com.supercell.scroll.consumableholidaypack1', 'Holiday pack $9.99'),
         ('com.supercell.scroll.consumableholidaypack2', 'Holiday pack $19.99'), ('com.supercell.scroll.consumablechinesenewyear0', 'Chinese New Yr pack $0.99'), ('com.supercell.scroll.consumablechinesenewyear1', 'Chinese New Yr pack $4.99'),
         ('com.supercell.scroll.consumablechinesenewyear2', 'Chinese New Yr pack $9.99')]

for item in names:
    print "WHEN package_id = '"+item[0]+"' THEN '"+item[1]+"'"