from utils import _set_paths
import redis
import json
_set_paths()

redisInstance = redis.Redis(host='localhost', port=6379, decode_responses=True)
from gmx_python_sdk.scripts.v2.get.get_funding_apr import GetFundingFee
from gmx_python_sdk.scripts.v2.gmx_utils import ConfigManager

class GetGMXv2Stats:

    def __init__(self, config, to_json, to_csv):
        self.config = config
        self.to_json = to_json
        self.to_csv = to_csv

    def get_funding_apr(self):

        return GetFundingFee(
            self.config
        ).get_data(
            to_csv=self.to_csv,
            to_json=self.to_json
        )

if __name__ == "__main__":

    to_json = False
    to_csv = False 

    config = ConfigManager(chain='arbitrum')
    config.set_config()

    stats_object = GetGMXv2Stats(
        config=config,
        to_json=to_json,
        to_csv=to_csv
    )
    funding_apr = stats_object.get_funding_apr()
    funding_aprstr = json.dumps(funding_apr, separators=(',', ':'))
    print("funding_apr")
    print(funding_apr)
    print(funding_aprstr)
    redisInstance.set('arbitrumFundingRates', funding_aprstr)