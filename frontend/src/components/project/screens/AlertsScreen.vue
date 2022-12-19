<template>
  <NavigationBar
    v-if="currentProject"
    :title="currentProject.title"
    hint="Set up alerts for your project with highly customized filters"
  >
    <BaseButton @click="goToCreateAlert" class="button">
      <PlusIcon /> Add Alert
    </BaseButton>
  </NavigationBar>

  <table v-if="alerts.length" class="table">
    <thead>
      <tr>
        <th>NAME</th>
        <th>CONDITIONS</th>
        <th>ASSIGNED USERS</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(item, index) in alerts"
        :key="'alert' + index"
        @click="goToUpdateAlert(item.id)"
      >
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

  <div class="no-alerts" v-else>No alerts created.</div>
</template>
<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/buttons/BaseButton'
import NavigationBar from '@/components/navigation/NavigationBar'
import TableSettingsButton from '@/components/buttons/TableSettingsButton'

import PlusIcon from '@/components/icons/PlusIcon'

export default {
  name: 'AlertsScreen',
  components: {
    PlusIcon,
    BaseButton,
    NavigationBar,
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
    goToCreateAlert() {
      this.$router.push({
        name: 'NewAlert',
      })
    },
    goToUpdateAlert(id) {
      this.$router.push({
        name: 'UpdateAlert',
        params: {
          alertId: id,
        },
      })
    },
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

.no-alerts {
  margin-top: 40px;

  color: var(--primary-text-color);
  font-size: 30px;
  font-weight: 400;
  line-height: 150%;
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
