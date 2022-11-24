<template>
  <NavigationBar
    v-if="currentProject"
    :title="currentProject.title"
    hint="Set up alerts for your project with highly customized filters"
  >
    <BaseButton class="button"><PlusIcon /> Add Alert</BaseButton>
  </NavigationBar>

  <table class="table">
    <thead>
      <tr>
        <th>
          <label class="container container-header">
            <input v-model="selectedProjects" type="checkbox" />
            <span class="checkmark"
              ><CheckRadioIcon class="checkmark-icon"
            /></span>
          </label>
        </th>
        <th>NAME</th>
        <th>CONDITIONS</th>
        <th>ASSIGNED USERS</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in alerts" :key="'alert' + index">
        <td>
          <label class="container">
            <input type="checkbox" />
            <span class="checkmark">
              <CheckRadioIcon class="checkmark-icon" />
            </span>
          </label>
        </td>
        <td>
          {{ item.title }}
        </td>
        <td>
          <span>{{ item.how_many_posts_to_send }}</span>
          <span>{{ item.triggered_on_every_n_new_posts }}</span>
        </td>
        <td>user</td>
        <td><TableSettingsButton :id="item.id" /></td>
      </tr>
    </tbody>
  </table>
</template>
<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/buttons/BaseButton'
import NavigationBar from '@/components/navigation/NavigationBar'
import TableSettingsButton from '@/components/buttons/TableSettingsButton'

import PlusIcon from '@/components/icons/PlusIcon'
import CheckRadioIcon from '@/components/icons/CheckRadioIcon'

export default {
  name: 'AlertsScreen',
  components: {
    PlusIcon,
    BaseButton,
    NavigationBar,
    CheckRadioIcon,
    TableSettingsButton,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  created() {
    this[action.GET_ALERTS](this.currentProject.id)
  },
  computed: {
    ...mapGetters({
      alerts: get.ALERTS,
    }),
  },
  methods: {
    ...mapActions([action.GET_ALERTS]),
  },
}
</script>

<style lang="scss" scoped>
.button-icon {
  margin-right: 7px;
}

.table {
  width: 100%;
  margin-top: 40px;

  border-collapse: separate;
  border-spacing: 0;

  cursor: pointer;

  thead {
    tr {
      th {
        padding-bottom: 10px;

        text-align: left;

        font-style: normal;
        font-weight: 400;
        font-size: 10px;
        line-height: 20px;
        color: var(--secondary-text-color);
      }

      th:first-child {
        padding: 0 0 0 29px;
      }
    }
  }

  tbody {
    tr {
      background: var(--secondary-bg-color);
      transition: background-color 2s;

      td {
        padding: 20px 0;

        border-top: 1px solid #2d2d31;

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: var(--primary-text-color);
      }

      &:hover {
        background: rgb(5, 95, 252);
        background: linear-gradient(
          90deg,
          rgba(5, 95, 252, 0.85) 0%,
          rgba(44, 44, 44, 1) 33%
        );
        transition: background-size 1s, background-color 1s;
      }
    }

    td:first-child {
      padding: 15px 0 15px 29px;

      border-left: 1px solid #2d2d31;
    }

    td:last-child {
      border-right: 1px solid #2d2d31;
    }

    tr:first-child td:first-child {
      border-left: 1px solid #2d2d31;
      border-top-left-radius: 15px;
    }

    tr:first-child td:last-child {
      border-right: 1px solid #2d2d31;
      border-top-right-radius: 15px;
    }

    tr:last-child td:first-child {
      border-left: 1px solid #2d2d31;
      border-bottom: 1px solid #2d2d31;
      border-bottom-left-radius: 15px;
    }

    tr:last-child td:last-child {
      border-right: 1px solid #2d2d31;
      border-bottom: 1px solid #2d2d31;
      border-bottom-right-radius: 15px;
    }

    tr:last-child td {
      border-bottom: 1px solid #2d2d31;
    }
  }
}

.container {
  position: relative;

  display: block;

  margin: 0 40px 20px 0;

  font-size: 22px;

  cursor: pointer;

  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.container input {
  position: absolute;

  height: 0;
  width: 0;

  opacity: 0;
  cursor: pointer;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  height: 20px;
  width: 20px;

  border: 1px solid #9198a7;
  border-radius: 4px;
  background-color: #2d2d31;
}

.container:hover input ~ .checkmark {
  background-color: #242529;
}

.container input:checked ~ .checkmark {
  border: none;
  background-color: #055ffc;
}

.container input ~ .checkmark > .checkmark-icon {
  display: none;
}

.container input:checked ~ .checkmark > .checkmark-icon {
  display: block;
}

.container input:checked ~ .checkmark:after {
  display: block;
}

.container-header {
  margin-bottom: 30px;
}

.type-icon {
  margin-right: 10px;
}

.type {
  display: flex;
  align-items: center;
}

.button {
  width: 136px;
  gap: 8px;
}
</style>
