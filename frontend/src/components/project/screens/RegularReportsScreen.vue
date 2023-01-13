<template>
  <NavigationBar
    v-if="currentProject"
    :title="currentProject.title"
    hint="Set up and manage reports"
  >
    <BaseButton @click="goToCreateRegularReport" class="button">
      Create New Report
    </BaseButton>
  </NavigationBar>

  <table v-if="reports.length" class="table">
    <thead>
      <tr>
        <th class="th-name">NAME</th>
        <th class="th-types">TYPES</th>
        <th class="th-recipient">RECIPIENT'S</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(item, index) in reports"
        :key="'alert' + index"
        @click="goToUpdateReport(item.id)"
      >
        <td>
          {{ item.title }}
        </td>
        <td>
          {{ getReportTypes(item) }}
        </td>
        <td>
          <MembersIconsBar :members="alertUsers(item.user)" />
        </td>
      </tr>
    </tbody>
  </table>

  <BlankPage v-else page-name="RegularReports" />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/buttons/BaseButton'
import MembersIconsBar from '@components/MembersIconsBar.vue'
import NavigationBar from '@/components/navigation/NavigationBar'
import BlankPage from '@/components/BlankPage'

export default {
  name: 'RegularReportsScreen',
  components: {
    BlankPage,
    BaseButton,
    MembersIconsBar,
    NavigationBar,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    ...mapGetters({
      reports: get.REGULAR_REPORTS,
      workspaces: get.WORKSPACES,
    }),
    workspaceMembers() {
      return this.workspaces.find(
        (el) => el.id === +this.$route.params.workspaceId
      ).members
    },
  },
  created() {
    if (!this.reports.length) {
      this[action.GET_REGULAR_REPORTS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([action.GET_REGULAR_REPORTS, action.GET_COMPANY_USERS]),
    goToCreateRegularReport() {
      this.$router.push({
        name: 'NewRegularReport',
      })
    },
    goToUpdateReport(id) {
      this.$router.push({
        name: 'UpdateRegularReport',
        params: {
          regularReportId: id,
        },
      })
    },
    alertUsers(alertUsersIds) {
      return this.workspaceMembers.filter((user) =>
        alertUsersIds.includes(user.id)
      )
    },
    getReportTypes(item) {
      const types = []
      if (item.hourly_enabled) types.push('Hourly')
      if (item.daily_enabled) types.push('Daily')
      if (item.weekly_enabled) types.push('Weekly')
      if (item.monthly_enabled) types.push('Monthly')
      return types.join(', ')
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

  .th-name {
    width: 40%;
  }
  .th-types {
    width: 30%;
  }
  .th-recipient {
    width: 30%;
  }

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
        padding: 20px 10px;

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

.type-icon {
  margin-right: 10px;
}

.type {
  display: flex;
  align-items: center;
}

.button {
  width: 176px;
  gap: 8px;
}

.clock-icon {
  margin-right: 10px;
}

.report-types {
  display: flex;
  flex-wrap: wrap;

  font-size: 14px;
}
</style>
