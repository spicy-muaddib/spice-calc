from flask import Flask,render_template,request
import pandas as pd
import numpy as np

application = Flask(__name__)

@application.route('/', methods=['POST','GET'])

def calculate():
    wbtc_total_debt = ''
    wbtc_address_debt = ''
    wbtc_vault_share = ''
    wbtc_max_qi_week = ''
    wbtc_max_qi_gauge = ''
    wbtc_value_one_pct = ''
    wbtc_profit_bribe = ''
    weth_total_debt = ''
    weth_address_debt = ''
    weth_vault_share = ''
    weth_max_qi_week = ''
    weth_max_qi_gauge = ''
    weth_value_one_pct = ''
    weth_profit_bribe = ''
    vault = ''
    wbtc_vault = ''
    weth_vault = ''
    address = ''
    vaults = ''

    if request.method=='POST' and 'address' in request.form:

        vaults=request.form.getlist('mycheckbox')
        address=request.form.get('address')

        for vault_num in vaults:
            if vault_num == '1': 
                vault = 'WBTC'
                wbtc_vault = 'WBTC'

                csv_file = "optimism.csv"
                df = pd.read_csv(csv_file,index_col=False) 
                df = df.query(f"tokenName == '{vault}'")

                qi_per_week = 180000
                wbtc_total_debt = df['debt'].sum()
                wbtc_address_debt = df.query(f"owner == '{address}'")['debt'].sum()
                wbtc_vault_share = wbtc_address_debt/wbtc_total_debt
                wbtc_max_qi_week = wbtc_vault_share*qi_per_week
                wbtc_max_qi_gauge = wbtc_max_qi_week * 2
                wbtc_value_one_pct = wbtc_max_qi_gauge/100
                wbtc_profit_bribe = wbtc_value_one_pct/2

            if vault_num == '2': 
                vault = 'WETH'
                weth_vault = 'WETH'

                csv_file = "optimism.csv"
                df = pd.read_csv(csv_file,index_col=False) 
                df = df.query(f"tokenName == '{vault}'")

                qi_per_week = 180000
                weth_total_debt = df['debt'].sum()
                weth_address_debt = df.query(f"owner == '{address}'")['debt'].sum()
                weth_vault_share = weth_address_debt/weth_total_debt
                weth_max_qi_week = weth_vault_share*qi_per_week
                weth_max_qi_gauge = weth_max_qi_week * 2
                weth_value_one_pct = weth_max_qi_gauge/100
                weth_profit_bribe = weth_value_one_pct/2

    return render_template("index.html",wbtc_total_debt=wbtc_total_debt,wbtc_address_debt=wbtc_address_debt,wbtc_vault_share=wbtc_vault_share,wbtc_max_qi_week=wbtc_max_qi_week,wbtc_max_qi_gauge=wbtc_max_qi_gauge,wbtc_value_one_pct=wbtc_value_one_pct,wbtc_profit_bribe=wbtc_profit_bribe,weth_total_debt=weth_total_debt,weth_address_debt=weth_address_debt,weth_vault_share=weth_vault_share,weth_max_qi_week=weth_max_qi_week,weth_max_qi_gauge=weth_max_qi_gauge,weth_value_one_pct=weth_value_one_pct,weth_profit_bribe=weth_profit_bribe,address=address,wbtc_vault=wbtc_vault,weth_vault=weth_vault)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()