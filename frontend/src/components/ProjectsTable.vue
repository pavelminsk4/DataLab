<template>
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
        <th>TYPE</th>
        <th>NAME</th>
        <th>KEYWORDS</th>
        <th>CREATOR</th>
        <th>ASSIGNED USERS</th>
        <th>DATE</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(item, index) in values"
        :key="index"
        @click="goToProject(item.id)"
      >
        <td>
          <label class="container">
            <input
              v-model="selectedProjects"
              :value="item.id"
              type="checkbox"
              :id="item.id"
            />
            <span class="checkmark">
              <CheckRadioIcon class="checkmark-icon" />
            </span>
          </label>
        </td>
        <td>
          <div class="type">
            <component class="type-icon" :is="item.source + 'RadioIcon'" />
            {{ item.source }}
          </div>
        </td>
        <td>{{ item.title }}</td>
        <td>
          <div v-if="item.keywords[0]" :class="item.keywords && 'keyword'">
            {{ item.keywords[0] }}
          </div>
          <div
            v-if="item.keywords[1]"
            :class="item.keywords[1] !== '' && 'keyword'"
          >
            {{ item.keywords[1] }}
          </div>
        </td>
        <td>{{ item.creator }}</td>
        <td>USERS</td>
        <td>{{ projectCreationDate(item.created_at) }}</td>
        <td><TableSettingsButton :id="item.id" /></td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import TableSettingsButton from '@/components/buttons/TableSettingsButton'

import PointsIcon from '@/components/icons/PointsIcon'
import CheckRadioIcon from '@/components/icons/CheckIcon'
import SocialRadioIcon from '@/components/icons/SocialRadioIcon'
import OnlineRadioIcon from '@/components/icons/OnlineRadioIcon'
import PremiumRadioIcon from '@/components/icons/PremiumRadioIcon'

export default {
  name: 'BaseTable',
  components: {
    TableSettingsButton,
    CheckRadioIcon,
    PremiumRadioIcon,
    OnlineRadioIcon,
    SocialRadioIcon,
    PointsIcon,
  },
  data() {
    return {
      selectedProjects: [],
      isOpenSettings: false,
    }
  },
  props: {
    values: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    projectCreationDate(date) {
      return new Date(date).toLocaleDateString('ro-RO')
    },
    goToProject(id) {
      this.$emit('go-to-project', id)
    },
  },
}
</script>

<style lang="scss" scoped>
.table {
  width: 100%;

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
      background: #242529;

      td {
        padding: 20px 0;

        border-top: 1px solid #2d2d31;

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: var(--primary-text-color);
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

.keyword {
  width: fit-content;
  padding: 2px 12px;

  border-radius: 8px;
  background: rgba(51, 204, 112, 0.2);

  font-weight: 400;
  font-size: 14px;
  line-height: 20px;

  color: #30f47e;
}

.keyword:first-child {
  margin-right: 6px;
}
</style>
