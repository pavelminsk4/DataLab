<template>
  <section class="widget">
    <template v-if="widgetData.user_name">
      <section class="account">
        <div class="account__user-section">
          <div class="account__avatar">
            <img :src="widgetData.user_picture" class="image" />
          </div>
          <div class="account__names">
            <div class="account__aliases">
              <h2>{{ widgetData.user_name }}</h2>
              <span>@{{ widgetData.user_alias }} </span>
            </div>
            <div>
              {{ widgetData.user_bio }}
            </div>
          </div>
        </div>
        <div class="account__info">
          <div class="info">
            <div class="info__item">
              <VerifiedIcon /> Twitter {{ isVerified(widgetData.verified) }}
            </div>
            <div class="info__item">
              <LocationIcon /> {{ widgetData.location }}
            </div>
            <div class="info__item">
              <StarIcon /> User value: {{ widgetData.user_value }}
            </div>
          </div>
        </div>
      </section>
      <section class="stats">
        <div
          v-for="(item, index) in statistics"
          :key="item.name"
          class="stats__item"
        >
          <component :is="`${icons[index]}Icon`" />
          <span>{{ item.name }}</span>
          <span class="stats__value">{{ item.value }}</span>
        </div>
      </section>
    </template>
    <div v-else class="spinner"><BaseSpinner /></div>
  </section>
</template>

<script>
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseSpinner from '@/components/BaseSpinner'

import VerifiedIcon from '@/components/icons/VerifiedIcon'
import LocationIcon from '@/components/icons/LocationIcon'
import StarIcon from '@/components/icons/StarIcon'
import ListIcon from '@/components/icons/ListIcon'
import MatrixDotsIcon from '@/components/icons/MatrixDotsIcon'
import TwitterIcon from '@/components/icons/TwitterIcon'
import CalendarWithBackgroundIcon from '@/components/icons/CalendarWithBackgroundIcon'
import EngagementIcon from '@/components/icons/EngagementIcon'
import HeartIcon from '@/components/icons/HeartIcon'
import RepostIcon from '@/components/icons/RepostIcon'
import GraphIcon from '@/components/icons/GraphIcon'

export default {
  props: {
    widgetData: {type: Object, required: true},
  },
  components: {
    VerifiedIcon,
    LocationIcon,
    StarIcon,
    ListIcon,
    MatrixDotsIcon,
    TwitterIcon,
    CalendarWithBackgroundIcon,
    EngagementIcon,
    HeartIcon,
    RepostIcon,
    GraphIcon,
    BaseSpinner,
  },
  computed: {
    statistics() {
      const data = {...this.widgetData.stats}

      return Object.keys(data).map((key) => {
        const itemName = capitalizeFirstLetter(
          key.replaceAll('_', ' ')
        ).replace('Avg', 'AVG')
        return {
          name: itemName,
          value: (+data[key]).toFixed(),
        }
      })
    },
  },
  created() {
    this.icons = [
      'List',
      'MatrixDots',
      'Twitter',
      'CalendarWithBackground',
      'Engagement',
      'Heart',
      'Repost',
      'Graph',
    ]
  },
  methods: {
    isVerified(cond) {
      return cond ? 'verified' : 'unverified'
    },
  },
}
</script>

<style lang="scss" scoped>
.widget {
  display: flex;

  position: relative;

  padding: 20px;
  gap: 20px;

  min-width: 100%;
  height: 100%;

  border-radius: 8px;
  background-color: var(--background-secondary-color);
  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);

  color: var(--typography-primary-color);
  .account {
    display: flex;
    flex-direction: column;
    justify-content: center;

    gap: 20px;

    width: 40%;

    &__avatar {
      width: fit-content;
      .image {
        width: 96px;
        border-radius: 50px;
      }
    }

    &__user-section {
      display: flex;
      gap: 12px;
    }
    &__names {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    &__aliases {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .info {
      display: flex;
      flex-wrap: wrap;

      gap: 10px;

      width: 80%;

      &__item {
        display: flex;
        align-items: center;
        gap: 10px;
      }
    }
  }

  .stats {
    display: grid;
    align-items: center;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 20px;

    width: 60%;

    &__item {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }

    &__value {
      font-size: 18px;
      font-weight: 700;
    }
  }

  .spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
  }
}
</style>
