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
        <td>
          <MembersIconsBar :members="alertsUsers(item.user)" />
        </td>
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
import MembersIconsBar from '@components/MembersIconsBar.vue'

import PlusIcon from '@/components/icons/PlusIcon'

export default {
  name: 'AlertsScreen',
  components: {
    PlusIcon,
    BaseButton,
    NavigationBar,
    MembersIconsBar,
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
      workspaces: get.WORKSPACES,
    }),
    currentWorkspace() {
      return this.workspaces.find(
        (el) => el.id === +this.$route.params.workspaceId
      )
    },
    workspaceMembers() {
      return this.currentWorkspace.members
    },
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
    alertsUsers(alertsUsersIds) {
      return this.workspaceMembers.filter((member) =>
        alertsUsersIds.includes(member.id)
      )
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

      td {
        padding: 20px 0;

        border-top: 1px solid var(--border-color);

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: var(--primary-text-color);
      }

      &:hover {
        background: var(--hover-circle-gradient);
        background-size: 200%;
        animation: var(--animation-hover-gradient);
        -webkit-animation: var(--animation-hover-gradient);
      }
    }

    td:first-child {
      padding: 15px 0 15px 29px;

      border-left: 1px solid var(--border-color);
    }

    td:last-child {
      border-right: 1px solid var(--border-color);
    }

    tr:first-child td:first-child {
      border-left: 1px solid var(--border-color);
      border-top-left-radius: 15px;
    }

    tr:first-child td:last-child {
      border-right: 1px solid var(--border-color);
      border-top-right-radius: 15px;
    }

    tr:last-child td:first-child {
      border-left: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      border-bottom-left-radius: 15px;
    }

    tr:last-child td:last-child {
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      border-bottom-right-radius: 15px;
    }

    tr:last-child td {
      border-bottom: 1px solid var(--border-color);
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
