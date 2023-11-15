<template>
  <nav class="sidebar-wrapper">
    <ul class="menu">
      <li
        v-for="(item, index) in navUrls"
        :key="'setting' + index"
        :class="['nav-item', item.routeName === routeName && 'active-setting']"
        @click="$emit('open-tab', item.routeName)"
      >
        <component
          :is="item.name + 'Icon'"
          :class="[item.routeName === routeName && 'active-icon', 'icon']"
        />

        <CustomText :text="item.name" class="sidebar-item-name" />
      </li>
    </ul>
  </nav>
</template>

<script>
import AnalyticsIcon from '@components/icons/AnalyticsIcon'
import SearchIcon from '@components/icons/SearchIcon'
import AlertsIcon from '@components/icons/AlertsIcon'
import ReportsIcon from '@components/icons/ReportsIcon'
import SummaryIcon from '@components/icons/SummaryIcon'
import DashboardIcon from '@components/icons/DashboardIcon'
import SentimentIcon from '@components/icons/SentimentIcon'
import DemographyIcon from '@components/icons/DemographyIcon'
import InfluencersIcon from '@components/icons/InfluencersIcon'
import OptimizationIcon from '@components/icons/OptimizationIcon'
import FollowersIcon from '@components/icons/FollowersIcon'
import PostsIcon from '@components/icons/PostsIcon'
import CustomText from '@components/CustomText'

export default {
  name: 'SideBar',
  components: {
    AlertsIcon,
    SearchIcon,
    ReportsIcon,
    AnalyticsIcon,
    SummaryIcon,
    DashboardIcon,
    SentimentIcon,
    DemographyIcon,
    InfluencersIcon,
    OptimizationIcon,
    PostsIcon,
    FollowersIcon,
    CustomText,
  },
  props: {
    navUrls: {type: Array, required: true},
  },
  computed: {
    routeName() {
      return this.$route.name
    },
  },
}
</script>

<style lang="scss" scoped>
.sidebar-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;

  width: 70px;
  height: 100%;
  margin-top: 52px;
  padding: 24px 12px 20px;

  background: var(--background-secondary-color);

  transition: width 400ms;

  &:hover {
    width: 210px;

    & + .wrap-all-the-things {
      transform: translateX(336px);
      max-width: 100%;
      opacity: 0.4;
    }

    .nav-item {
      gap: 8px;
      border-radius: 18px;

      @for $i from 1 through 4 {
        &:nth-of-type(#{$i}) {
          .sidebar-item-name {
            border-radius: 18px;
            transition-delay: 100ms * $i;
          }
        }
      }
    }

    .sidebar-item-name {
      width: 100%;
      text-indent: 0;
      border-radius: 18px;
      opacity: 1;
    }
  }
}

.nav-item {
  position: relative;
  clear: both;

  display: flex;
  align-items: center;

  padding: 12px;
  margin-bottom: 10px;
  transition: background 400ms;

  cursor: pointer;

  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  color: var(--typography-secondary-color);

  .sidebar-item-name {
    position: relative;

    align-items: center;

    width: 0;

    z-index: 0;
    opacity: 0;

    text-indent: -10em;
    white-space: nowrap;

    border-radius: 18px;
    transition: text-indent 400ms ease-in-out;
    transition: opacity 0.1s ease-in-out;

    color: var(--typography-title-color);
  }

  &:hover {
    background-color: var(--primary-active-color);

    &:before {
      background-color: var(--button-primary-hover-color);
    }

    .icon {
      color: var(--button-primary-color);
    }
  }
}

.active-setting {
  position: relative;

  border-radius: 18px;
  background-color: var(--primary-active-color);

  color: var(--typography-title-color);

  &::before {
    position: absolute;
    left: -13px;

    content: ' ';

    height: 100%;
    width: 3px;

    background-color: var(--primary-color);
  }
}

.active-icon {
  color: var(--primary-color);
}

.menu {
  margin: 0;
  padding: 0;
  list-style: none;
}

.icon {
  position: relative;
  z-index: 1;
  transition: 400ms;

  width: 20px;
  height: 20px;
}

.wrap-all-the-things {
  height: 100%;
  min-height: 100%;
  margin-top: 0;
  padding-left: 140px;

  transition: transform 400ms, opacity 400ms;
}
</style>
