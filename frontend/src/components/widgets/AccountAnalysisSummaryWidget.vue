<template>
  <section class="widget">
    <template v-if="!isAllFieldsEmpty(widgetData.user_name)">
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
              <VerifiedIcon />
              <CustomText
                :text="`Twitter ${isVerified(widgetData.verified)}`"
              />
            </div>
            <div class="info__item">
              <LocationIcon /> {{ widgetData.location }}
            </div>
            <div class="info__item">
              <StarIcon /> <CustomText tag="span" text="User value:" />
              {{ widgetData.user_value }}
            </div>
          </div>
        </div>
      </section>
      <section class="stats">
        <div v-for="item in stats" :key="item.name" class="stats__item">
          <component
            :is="`${item.iconName}Icon`"
            :class="[item.iconName.toLowerCase(), 'icon']"
          />
          <CustomText tag="span" :text="item.name" />
          <span class="stats__value">{{ item.value?.toFixed() }}</span>
        </div>
      </section>
    </template>
    <div v-else class="spinner"><BaseSpinner /></div>
  </section>
</template>

<script>
import {isAllFieldsEmpty} from '@/lib/utilities'

import BaseSpinner from '@/components/BaseSpinner'
import VerifiedIcon from '@/components/icons/VerifiedIcon'
import LocationIcon from '@/components/icons/LocationIcon'
import StarIcon from '@/components/icons/StarIcon'
import NewPostIcon from '@/components/icons/NewPostIcon'
import LanguageSymbolsIcon from '@/components/icons/LanguageSymbolsIcon'
import CountryIcon from '@/components/icons/CountryIcon'
import AuthorIcon from '@/components/icons/AuthorIcon'
import NeutralIcon from '@/components/icons/NeutralIcon'
import NegativeIcon from '@/components/icons/NegativeIcon'
import PositiveIcon from '@/components/icons/PositiveIcon'
import GraphIcon from '@/components/icons/GraphIcon'
import ListIcon from '@/components/icons/ListIcon'
import MatrixDotsIcon from '@/components/icons/MatrixDotsIcon'
import TwitterIcon from '@/components/icons/TwitterIcon'
import CalendarIcon from '@/components/icons/CalendarIcon'
import EngagementIcon from '@/components/icons/EngagementIcon'
import HeartIcon from '@/components/icons/HeartIcon'
import RetweetIcon from '@/components/icons/RetweetIcon'
import CustomText from '@/components/CustomText'

export default {
  name: 'AccountAnalysisSummaryWidget',
  props: {
    widgetData: {type: Object, required: true},
    stats: {type: Array, required: true},
  },
  components: {
    CustomText,
    BaseSpinner,
    VerifiedIcon,
    LocationIcon,
    StarIcon,
    NewPostIcon,
    LanguageSymbolsIcon,
    CountryIcon,
    AuthorIcon,
    NeutralIcon,
    NegativeIcon,
    PositiveIcon,
    GraphIcon,
    ListIcon,
    MatrixDotsIcon,
    TwitterIcon,
    CalendarIcon,
    EngagementIcon,
    HeartIcon,
    RetweetIcon,
  },
  methods: {
    isVerified(cond) {
      return cond ? 'verified' : 'unverified'
    },
    isAllFieldsEmpty,
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

.icon {
  height: 28px;
  width: 28px;
  padding: 6px;

  border-radius: 4px;

  color: var(--button-text-color);
}

.neutral {
  background-color: var(--neutral-primary-color);
}

.negative {
  background-color: var(--negative-primary-color);
}

.positive {
  background-color: var(--positive-primary-color);
}

.newpost {
  background-color: rgb(46, 168, 221);
}

.languagesymbols {
  background-color: rgb(117, 70, 255);
}

.country {
  background-color: #a0b8be;
}

.author {
  background-color: #ec809d;
}

.graph {
  background-color: #fc732d;
}

.calendar {
  background-color: #a0b8be;
}

.twitter {
  padding: 0;
}

.list {
  background-color: #2ea8dd;
}

.matrixdots {
  background-color: #57c7b3;
}

.heart {
  background-color: #ed2549;
}

.engagement {
  background-color: #7546ff;
}

.retweet {
  background-color: #3088f0;
}
</style>
