from otree.api import *

doc = """
Strategy method for negotiation game.
"""


class C(BaseConstants):
    NAME_IN_URL = 'distributive_bargaining_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 50
    INSTRUCTIONS_FILE = __name__ + '/instructions.html'
    ENDOWMENT = cu(50)
    OFFER_CHOICES = currency_range(0, ENDOWMENT, 1)
    OFFER_CHOICES_COUNT = len(OFFER_CHOICES)

    POSSIBLE_ALLOCATIONS = []
    for OFFER in OFFER_CHOICES:
        POSSIBLE_ALLOCATIONS.append(dict(p1_amount=OFFER, p2_amount=ENDOWMENT - OFFER))




class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    print("creating_session method")
    print("round number " + str(subsession.round_number))



class Group(BaseGroup):
    print(C.OFFER_CHOICES)
    amount_offered = models.CurrencyField(choices=C.OFFER_CHOICES)
    offer_accepted = models.BooleanField(
        label="Would you accept the offer?",
        widget=widgets.RadioSelect,
        # note to self: remove this once i release bugfix
        choices=[[False, 'No'], [True, 'Yes']],
        initial=False
    )

    make_new_offer = models.BooleanField(
        label="Would you make a new offer?",
        widget=widgets.RadioSelect,
        # note to self: remove this once i release bugfix
        choices=[[False, 'No'], [True, 'Yes']],
        initial=True)
    


def set_payoffs(group: Group):    
    p1, p2 = group.get_players()
    amount_offered = group.amount_offered
    if group.offer_accepted:
        p1.payoff = C.ENDOWMENT - amount_offered
        p2.payoff = amount_offered 
    else:
        p1.payoff = 0
        p2.payoff = 0
        
    


class Player(BasePlayer):
    pass


class P1(Page):
    form_model = 'group'
    #form_fields = ['amount_offered']

    @staticmethod
    def get_form_fields(player):
        if player.round_number > 1:
            return ['amount_offered', 'offer_accepted']
        else:
            return ['amount_offered']


    @staticmethod
    def is_displayed(player: Player):
        if player.round_number > 1:
            #self.form_fields.append('offer_accepted')
            prev_group = player.group.in_round(player.round_number - 1)
            player.group.amount_offered = prev_group.amount_offered
            player.group.offer_accepted = prev_group.offer_accepted
            player.group.make_new_offer = prev_group.make_new_offer
        return player.id_in_group == 1 and player.group.make_new_offer
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.group.offer_accepted:
            player.group.make_new_offer = False



class P1ContributionWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.group.make_new_offer



class P2(Page):
    form_model = 'group'
    form_fields = ['offer_accepted', 'make_new_offer', 'amount_offered']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2 and player.group.make_new_offer

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.group.offer_accepted:
            player.group.make_new_offer = False


class P2ContributionWaitPage(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1 and player.group.make_new_offer

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    title_text = "Thank you"
    body_text = (
        "You can close this page. When the other player arrives, the payoff will be calculated."
    )

    @staticmethod
    def is_displayed(player: Player):
        return not player.group.make_new_offer



class Results(Page):
    pass

    @staticmethod
    def is_displayed(player: Player):
        return not player.group.make_new_offer

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if not player.group.make_new_offer:
            return 'payment_info'

page_sequence = [
    P1,
    P1ContributionWaitPage,
    P2,
    P2ContributionWaitPage,
    ResultsWaitPage,
    Results,
]
