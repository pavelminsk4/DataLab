<template>
  <table v-if="workspaces" class="table">
    <thead>
      <tr>
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
        <td>
          <img :src="memberPhoto(item.creator)" class="cart-image" />
        </td>
        <td>PHOTO</td>
        <td>{{ projectCreationDate(item.created_at) }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import PointsIcon from '@/components/icons/PointsIcon'
import CheckRadioIcon from '@/components/icons/CheckIcon'
import SocialRadioIcon from '@/components/icons/SocialRadioIcon'
import OnlineRadioIcon from '@/components/icons/OnlineRadioIcon'
import PremiumRadioIcon from '@/components/icons/PremiumRadioIcon'

export default {
  name: 'ProjectsTable',
  components: {
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
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    currentWorkspace() {
      return this.workspaces.filter(
        (el) => el.id === +this.$route.params.workspaceId
      )
    },
    members() {
      return this.currentWorkspace[0].members
    },
  },
  methods: {
    memberPhoto(id) {
      return this.members.filter((el) => el.id === id)[0].user_profile.photo
    },
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
      background: var(--secondary-bg-color);

      &:hover {
        background: var(--hover-circle-gradient);
        background-size: 200%;
        animation: hover-gradient 0.3s ease;
        -webkit-animation: hover-gradient 0.3s ease;
      }

      td {
        padding: 20px 0;

        border-top: 1px solid var(--border-color);

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: var(--primary-text-color);

        &:first-child {
          padding: 15px 0 15px 29px;

          border-left: 1px solid var(--border-color);
        }

        &:last-child {
          border-right: 1px solid var(--border-color);
        }
      }
    }

    tr:first-child td {
      &:first-child {
        border-left: 1px solid var(--border-color);
        border-top-left-radius: 15px;
      }
      &:last-child {
        border-right: 1px solid var(--border-color);
        border-top-right-radius: 15px;
      }
    }

    tr:last-child td {
      border-bottom: 1px solid var(--border-color);

      &:first-child {
        border-left: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
        border-bottom-left-radius: 15px;
      }
      &:last-child {
        border-right: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
        border-bottom-right-radius: 15px;
      }
    }
  }
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
  background-color: var(--border-color);
}

.type-icon {
  margin-right: 10px;
}

.type {
  display: flex;
  align-items: center;
}

.cart-image {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 0;
  flex-shrink: 0;

  width: 22px;
  height: 22px;
  margin-right: 12px;

  border-radius: 100%;
  border: 1px solid var(--secondary-text-color);

  background-color: white;

  font-size: 10px;

  &:not(:first-child) {
    margin-left: -10px;
  }
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
