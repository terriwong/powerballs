jackpot = ['16', '19', '32', '34', '57', '13']


def powerballs(tickets_data_filename):
    """Find prize(s) in tickets, if any."""

    jackpot_white_list = jackpot[0:5]
    jackpot_white_set = set(jackpot_white_list)
    #since order doesn't matter, transform to set
    jackpot_red = jackpot[5]

    tickets_data = open(tickets_data_filename)

    for line in tickets_data:
        line = line.rstrip()
        nums = line.split('|')

        ticket_id = nums[0]
        ticket_white_list = nums[1:6]
        ticket_white_set = set(ticket_white_list)
        #since order doesn't matter, transform to set
        intersection = jackpot_white_set & ticket_white_set
        ticket_red = nums[-1]

        if len(intersection) == 5 and jackpot_red == ticket_red:
            print "Ticket No.%s is winning a Grand Prize!" % (ticket_id)
        elif len(intersection) == 5 and jackpot_red != ticket_red:
            print "Ticket No.%s is winning $1,000,000!" % (ticket_id)
        elif len(intersection) == 4 and jackpot_red == ticket_red:
            print "Ticket No.%s is winning $50,000!" % (ticket_id)
        elif len(intersection) == 4 and jackpot_red != ticket_red:
            print "Ticket No.%s is winning $100!" % (ticket_id)
        elif len(intersection) == 3 and jackpot_red == ticket_red:
            print "Ticket No.%s is winning $100!" % (ticket_id)
        elif len(intersection) == 3 and jackpot_red != ticket_red:
            print "Ticket No.%s is winning $7!" % (ticket_id)
        elif len(intersection) == 2 and jackpot_red == ticket_red:
            print "Ticket No.%s is winning $7!" % (ticket_id)
        elif len(intersection) == 1 and jackpot_red == ticket_red:
            print "Ticket No.%s is winning $4!" % (ticket_id)
        elif len(intersection) == 0 and jackpot_red == ticket_red:
            print "Ticket No.%s is winning $4!" % (ticket_id)
        # else:
        #     print "Nothing."

    tickets_data.close()

powerballs("powerballs.txt")
