<template>
  <BaseTable :table-header="tableHeader" :hasCheckbox="false">
    <tr v-for="(item, index) in followers" :key="index" :id="item.index">
      <td>
        <div class="user-name">
          <img :src="item.user_img" class="img" />
          <div class="title">
            <span class="name">{{ item.user_name }}</span>
            <span class="alias">{{ item.user_alias }}</span>
          </div>
        </div>
      </td>
      <td><BaseChips :chips-type="item.gender" /></td>
      <td class="table-item interactions">{{ item.interactions }}</td>
      <td class="table-item">{{ item.avg_of_engagements }}</td>
      <td class="table-item">{{ item.followers }}</td>
      <td class="table-item">{{ item.following }}</td>
      <td>{{ item.bio }}</td>
    </tr>
  </BaseTable>
</template>

<script>
import BaseChips from '@/components/BaseChips'
import BaseTable from '@/components/common/BaseTable'

export default {
  name: 'AccountAnalysisFollowersScreen',
  props: {
    currentProject: {type: Object, required: true},
  },
  components: {BaseTable, BaseChips},
  data() {
    return {
      selectedAlerts: [],
    }
  },
  computed: {
    followers() {
      return [
        {
          user_name: 'Richard Teston',
          user_alias: '@richard',
          user_img:
            'https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dXNlcnxlbnwwfHwwfHw%3D&w=1000&q=80',
          gender: 'male',
          interactions: 24,
          avg_of_engagements: 24,
          followers: 2434,
          following: 1945,
          bio: 'Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston Richard Teston',
        },
      ]
    },
  },
  created() {
    this.tableHeader = [
      {name: 'User', width: '18%'},
      {name: 'Gender', width: '10%'},
      {name: 'Interactions', width: '10%'},
      {name: 'Avg of engagements', width: '14%'},
      {name: 'Followers', width: '9%'},
      {name: 'Following', width: '9%'},
      {name: 'Bio', width: '30%'},
    ]
  },
}
</script>

<style lang="scss" scoped>
.user-name {
  display: flex;
  align-items: center;
  gap: 8px;

  height: 100%;
  .img {
    width: 24px;
    height: 24px;

    border-radius: 100%;
  }

  .title {
    display: flex;
    flex-direction: column;

    color: var(--typography-primary-color);

    .name {
      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
    }
    .alias {
      font-style: normal;
      font-weight: 400;
      font-size: 11px;
      line-height: 12px;
    }
  }
}

.table-item {
  text-align: center;
}

.interactions {
  background-color: var(--primary-active-color);
}
</style>
