from scr.funcs import open_file, sort_date, format_date, hide_accounts_data, bill_output

file = open_file()

last_five_executed_operations = sort_date(file)

change_date_format = format_date(last_five_executed_operations)

hidden_data = hide_accounts_data(change_date_format)

bill_format = bill_output(hidden_data)


