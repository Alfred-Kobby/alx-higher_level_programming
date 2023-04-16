0-select_states.py file: python sql to select all states

states
2-my_filter_states.py file: displays states where name matches input

3-my_safe_filter_states.py file: display states that matches input but safe from sql injection

4-cities_by_state.py file: display cities with only one execute call

5-filter_cities.py file: display cities by using state name with one execute call

model_state.py base model for state with ORM

7-model_state_fetch_all.py file: list all states object with ORM

8-model_state_fetch_first.py file: display the first state in db using ORM

9-model_state_filter_a.py file: list all states that starts with letter a using ORM

10-model_state_my_get.py file: prints the state object with the name passed to it as arguement using ORM

11-model_state_insert.py file: adds/insert states object into database using ORMs

12-model_state_update_id_2.py file: update the name of a state object using ORM

13-model_state_delete_a.py file: deletes all state objects that contains the letter a using ORM

model_city.py base model for cities using ORM

14-model_city_fetch_by_state.py file: displays cities fetched by state id using ORM

relationship_city.py file: improved model of city model

relationship_state.py file: improved model of state model

100-relationship_states_cities.py file: creates states with city

101-relationship_states_cities_list.py file: list all states objects and their corresponding cities