import logging

class Ring:
    def __init__(self, llm_list, max_attempts=5, retry_delay=5, throttle_delay=5, log_enabled=True, wip_save=True):
        # Validate the llm_list
        if not llm_list:
            raise ValueError("Failed initialising Ring, llm_list is not declared by the user")
        if not isinstance(llm_list, list) or not all(isinstance(llm, dict) for llm in llm_list):
            raise ValueError("""Failed initialising Ring, llm_list does not align with expected format. Please pass llm_list in the format 
                [{"service":"OpenAIChat", 
                  "access_token":"enter-your-token-here",
                  "identifier":"identifier-for-the-account-used-for-the-token"},
                  {"service":"BardChat", 
                  "access_token":"enter-your-token-here",
                  "identifier":"identifier-for-the-account-used-for-the-token"},
                  {"service":"EdgeChat",}]""")
        for llm in llm_list:
            if 'service' not in llm:
                raise ValueError("Failed initialising Ring, service attribute is not declared by the user in the dictionaries passed in llm_list")
            if llm['service'] in ["OpenAIChat", "BardChat"] and (not llm.get('access_token')):
                raise ValueError("Failed initialising Ring, access_token attribute is not declared by the user in the dictionaries passed in llm_list for OpenAIChat or BardChat")
        
        self.llm_list = llm_list
        self.max_attempts = max_attempts
        self.retry_delay = retry_delay
        self.throttle_delay = throttle_delay
        self.log_enabled = log_enabled
        self.wip_save = wip_save
        self.output_dataframe = None

        # Set up logging
        if self.log_enabled:
            logging.basicConfig(filename='ring_log.log', filemode='a', level=logging.INFO, 
                                format='%(asctime)s - %(levelname)s - %(message)s')
            logging.info("Ring initialised")
            