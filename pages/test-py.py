"""
Team distribution test page.
"""

import copy
import streamlit as st

from classes.data_source import TeamStats
from classes.visual import DistributionPlot
from utils.page_components import add_common_page_elements


sidebar_container = add_common_page_elements()
st.divider()

teams = TeamStats()

metrics = [
    "loss_proportion",
    "create_proportion",
    "direct_proportion",
]
teams.calculate_statistics(metrics=metrics)

team = copy.deepcopy(teams)

with sidebar_container:
    team.select_and_filter(
        column_name="team_name",
        label="Team",
    )
    team = team.to_data_point()

st.subheader("Team Distribution")

visual = DistributionPlot(metrics[::-1], labels=["Lower", "Average", "Higher"])
visual.add_title_from_player(team)
visual.add_players(teams, metrics=metrics)
visual.add_player(team, len(teams.df), metrics=metrics)
visual.show()
