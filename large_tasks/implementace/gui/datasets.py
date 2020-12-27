from classes.Iris import Iris
from classes.MallCustomers import MallCustomers
from classes.BankMarketing import BankMarketing, BankMarketingClientWithSocialEconomic, BankMarketingClient

datasets = {
    "Iris": Iris(),
    "MallCustomers": MallCustomers(),
    "BankMarketingClient": BankMarketingClient(),
    "BankMarketingClientSocialEconomic": BankMarketingClientWithSocialEconomic()
}